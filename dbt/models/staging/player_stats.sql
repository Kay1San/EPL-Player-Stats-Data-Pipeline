select 
    full_name as Name,
    team_name as Team,
    season as Season,
    element_type as Role,
    goals_scored as Goals, 
    assists as Assists, 
    goals_and_assists as GoalsAndAssists, 
    goals_conceded as GoalsConceded,
    clean_sheets as CleanSheets,
    influence as Influence,
    creativity as Creativity, 
    transfers_in as TotalTransferSpend, 
    yellow_cards as YellowCards,
    red_cards as RedCards,
    value_season as ValueSeason,
    now_cost as Cost
    
from 
    {{ ref('stg_table_bq_epl_player_stats') }}

