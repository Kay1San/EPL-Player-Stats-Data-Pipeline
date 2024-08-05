select 
    team_name as Team,
    season as Season,
    SUM(goals_scored) as Goals, 
    SUM(assists) as Assists, 
    SUM(goals_and_assists) AS GoalsAndAssists, 
    SUM(goals_conceded) AS GoalsConceded, 
    SUM(transfers_in) AS TotalTransferSpend, 
    SUM(transfers_out) AS TotalTransferIncome
from 
    {{ ref('stg_table_bq_epl_player_stats') }}
group by 
    Team, Season
