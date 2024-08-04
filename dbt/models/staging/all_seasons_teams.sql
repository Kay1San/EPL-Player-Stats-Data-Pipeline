select 
    team_name,
    SUM(goals_scored) as t_goals, 
    SUM(assists) as t_assists, 
    SUM(goals_and_assists) as t_g_a, 
    SUM(goals_conceded) as t_goals_conceded, 
    SUM(transfers_in) as sum_bought, 
    SUM(transfers_out) as sum_sold
from 
    {{ ref('stg_table_bq_epl_player_stats') }}
group by 
    team_name
