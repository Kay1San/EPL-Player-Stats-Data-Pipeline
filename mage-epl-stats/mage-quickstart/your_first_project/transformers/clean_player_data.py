import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test



@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    
    url_old_teams = "https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/master_team_list.csv"
    old_teams_df = pd.read_csv(url_old_teams)


    data = data[data['minutes'] > 0]
    data = pd.merge(data, old_teams_df, on=['season', 'team'], how='left')


    url_current_teams = "https://raw.githubusercontent.com/vaastav/Fantasy-Premier-League/master/data/2023-24/teams.csv"
    current_teams_df = pd.read_csv(url_current_teams)
    current_teams_df = current_teams_df.rename(columns={"id": "team", "name": "new_team_name"})
    #print(current_teams_df['team'].unique())

    
    current_data = data[data['season'] == "2023-24"]
    #print(current_teams_df['team'].unique())
    
    current_data = pd.merge(current_data, current_teams_df[['team', 'new_team_name']], how='left', on='team')
    current_data = current_data.drop(columns=['team_name'])
    current_data = current_data.rename(columns={"new_team_name" : "team_name"})
    
    #print(current_data.head())


    data = pd.concat([
    data[data['season'] != "2023-24"],  
    current_data  
    ])
   
    

    data = data.drop(columns=['code', 'cost_change_event', 'bps', 'chance_of_playing_next_round', 'chance_of_playing_this_round', 
                             'cost_change_event_fall', 'cost_change_start', 'cost_change_start_fall', 'bonus', 'dreamteam_count', 'team',
                             'ea_index', 'ep_next', 'ep_this', 'event_points', 'form', 'ict_index', 'in_dreamteam',
                             'news', 'photo', 'selected_by_percent', 'special', 'squad_number', 'threat', 'transfers_in_event',
                             'value_form', 'web_name', 'news_added', 'creativity_rank', 'creativity_rank_type', 'ict_index_rank',
                             'influence_rank', 'influence_rank_type', 'threat_rank', 'threat_rank_type', 'corners_and_indirect_freekicks_order',
                             'corners_and_indirect_freekicks_text', 'direct_freekicks_order', 'direct_freekicks_text', 'penalties_order',
                             'penalties_text', 'expected_assists', 'expected_assists_per_90', 'expected_goal_involvements', 'expected_goal_involvements_per_90',
                             'expected_goals', 'expected_goals_conceded', 'expected_goals_conceded_per_90', 'expected_goals_per_90',
                             'expected_goals_per_90', 'form_rank', 'form_rank_type', 'goals_conceded_per_90', 'now_cost_rank', 'now_cost_rank_type',
                             'points_per_game_rank', 'points_per_game_rank_type', 'selected_rank', 'selected_rank_type', 'starts', 'starts_per_90',
                             'loaned_in', 'loaned_out', 'loans_in', 'loans_out', 'status', 'transfers_out_event', 'team_code'])

    data['full_name'] = data['first_name'] + ' ' +  data['second_name']
    data = data.drop(columns = ['first_name', 'second_name'])

    roles = {1: 'GK', 2: 'DEF', 3: 'MID', 4: 'FWD'}

   
    
    def get_role(role):
        return roles.get(role, role)
    
    data['element_type'] = data['element_type'].apply(get_role)

    data['goals_and_assists'] = data['assists'] + data['goals_scored']

    data = data[['full_name', 'season', 'team_name', 'element_type', 'goals_scored', 'assists', 'goals_and_assists', 'goals_conceded', 'transfers_in', 
                'transfers_out', 'clean_sheets', 'clean_sheets_per_90', 'saves_per_90',
                'creativity', 'influence', 'minutes', 'now_cost', 'own_goals', 'penalties_missed', 'penalties_saved', 'points_per_game',
                'saves', 'red_cards', 'yellow_cards', 'total_points', 'value_season', 'ict_index_rank_type']]

    print(data.tail())
    
    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    if (output['team_name'] == "").all():
        raise ValueError("empty team name")
