with 

source as (

    select * from {{ source('staging', 'table-bq-epl-player-stats') }}

),

renamed as (

    select
        full_name,
        season,
        team_name,
        element_type,
        goals_scored,
        assists,
        goals_and_assists,
        goals_conceded,
        transfers_in,
        transfers_out,
        clean_sheets,
        clean_sheets_per_90,
        saves_per_90,
        creativity,
        influence,
        minutes,
        now_cost,
        own_goals,
        penalties_missed,
        penalties_saved,
        points_per_game,
        saves,
        red_cards,
        yellow_cards,
        total_points,
        value_season,
        ict_index_rank_type

    from source

)

select * from renamed
