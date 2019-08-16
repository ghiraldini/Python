#!/usr/env/python3

import statsapi as mlb2
import time
import datetime as dt
import queue


class MlbWorker:
    def __init__(self):

        # pay per game ($162/team = $2 on each game)
        self.ppg = 2
        self.total_payout = 0

        # count number of days for pot build up
        self.count = 0
        self.days = 0

        # Get todays date for statsapi `get` call
        self.today = dt.datetime.today().strftime('%m/%d/%Y')

        # Default teams - will be overridden by GUI thread
        self.team_1 = "Texas Rangers"
        self.team_2 = "St. Louis Cardinals"

        # start of opening day
        self.opening_day = "03/28/2019"
        # Start timer of program
        self.start = time.time()
        # Init Queue for messaging GUI Thread
        self.queue = queue.Queue()
        # this->thread has updates to send to GUI
        self.update = True

    # Send Queue to GUI thread
    def get_q(self):
        return self.queue

    # Tells GUI Thread we are still/done updating
    def needs_update(self):
        return self.update

    # Get Team names from GUI Thread
    def set_teams(self, t1, t2):
        self.team_1 = t1
        self.team_2 = t2

    """
    Worker Thread
    Each game adds $2 to the pot
    Winner gets all games added to the pot from that day
    Pot is reset to $2 on the 1st game of the next day
    Mulitple winners in the same day split the pot (1st game & last game of same day get same amount)
    """
    def do_work_mlb_stats(self):
        self.queue.put("")
        gd = ""
        flag_winner = False
        my_team_won = False
        winners = []

        # Get all games since opening day through today
        games = mlb2.schedule(start_date=self.opening_day, end_date=self.today)

        # Cycle through each game in list
        for x in games:

            # End of day
            if x['game_date'] != gd:
                gd = x['game_date']
                self.days += 1

                # Check if there was a winner(s) that day
                if flag_winner:
                    for winner in winners:
                        if my_team_won:
                            self.queue.put("YOU WON!!! - " + winner + "\t\t\tPayout: {}"
                                           .format(self.total_payout / winners.__len__()))
                        else:
                            self.queue.put(winner + "\t\t\tPayout: {}".format(self.total_payout / winners.__len__()))

                    self.queue.put(
                            "--------------------------------------------------------------------------------------")
                    self.count = 1
                    self.total_payout = self.count * self.ppg
                    winners.clear()
                    self.days = 1
                    flag_winner = False
                    my_team_won = False

            # self.queue.put(x['summary'] + "\t\tPot: " + str(self.total_payout))

            # Check if 13-Run Game happened
            if x['away_score'] == 13 or x['home_score'] == 13:

                # We have a winner!
                flag_winner = True

                # Check Teams we're invested in
                if x['home_name'] == self.team_1 or x['home_name'] == self.team_2 and x['home_score'] == 13 \
                        or x['away_name'] == self.team_1 or x['away_name'] == self.team_2 and x['away_score'] == 13:
                    winners.append(x['summary'])
                    my_team_won = True

                # Someone else has won
                else:
                    winners.append(x['summary'])

            # No Winner - keep updating money pot
            else:
                self.count += 1
                self.total_payout = self.count * self.ppg

        # End of loop - display some details
        el = time.time() - self.start
        self.queue.put("")
        self.queue.put("Elaspsed Time: {}".format(el))
        self.queue.put("")
        self.queue.put("Days since last winner: {}, Games since last winner: {}".format(self.days, self.count))
        self.queue.put("Money in the pot: {}".format(self.total_payout))

        time.sleep(1)

        # Tell GUI thread we're done sending data through Queue
        self.update = False
