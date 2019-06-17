
import mlbgame as mlb
import time

# pay per game ($162/team = $2 on each game)
ppg = 2
total_payout = 0

# count number of days for pot build up
count = 0

# TODO: make this automatic using datetime lib
curr_month = 6

# start in April (04) opening day
m = 4

start = time.time()

while m <= curr_month:
    print("--------------------------------------------------")
    print("Games of 2019-{}".format(m))
    print("--------------------------------------------------")
    month = mlb.games(2019, m)
    curr_day = 1
    for day in month:
        for games in day:
            runs_away = games.away_team_runs
            runs_home = games.home_team_runs
            if runs_away == 13 or runs_home == 13:
                if games.away_team == "Cardinals" or games.home_team == "Cardinals" or games.away_team == "Rangers" or \
                        games.home_team == "Rangers":
                    print("\t13 RUN GAME 2019/{}/{} - Payout = ${}<-----------".format(m, curr_day, total_payout))
                    print("\t\t{}-{}, {} vs {}".format(runs_away, runs_home, games.away_team, games.home_team))
                else:
                    print("\t13 RUN GAME 2019/{}/{} - Payout = ${}".format(m, curr_day, total_payout))
                    print("\t\t{}-{}, {} vs {}".format(runs_away, runs_home, games.away_team, games.home_team))
                count = 0
                total_payout = 0
            else:
                count += 1
                total_payout = count * ppg
        curr_day += 1
    m += 1

end = time.time()

print("Time for lookup: {} minutes".format((end - start)/60.0))
