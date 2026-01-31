def main() -> None:
    """
    Run the Game Analytics Dashboard and demonstrate list,
    dict, and set comprehensions.
    """
    print('=== Game Analytics Dashboard ===')
    data = {
            'players': {
                'alice': {'level': 41, 'total_score': 2824,
                          'sessions_played': 13,
                          'favorite_mode': 'ranked',
                          'achievements_count': 5},
                'bob': {'level': 16, 'total_score': 4657,
                        'sessions_played': 27,
                        'favorite_mode': 'ranked',
                        'achievements_count': 2},
                'charlie': {'level': 44, 'total_score': 9935,
                            'sessions_played': 21,
                            'favorite_mode': 'ranked',
                            'achievements_count': 7},
                'diana': {'level': 3, 'total_score': 1488,
                          'sessions_played': 21,
                          'favorite_mode': 'casual',
                          'achievements_count': 4},
                'eve': {'level': 33, 'total_score': 1434,
                        'sessions_played': 81,
                        'favorite_mode': 'casual',
                        'achievements_count': 7},
                'frank': {'level': 15, 'total_score': 8359,
                          'sessions_played': 85,
                          'favorite_mode': 'competitive',
                          'achievements_count': 1}
                },
            'sessions': [
                {'player': 'bob', 'duration_minutes': 94, 'score': 1831,
                 'mode': 'competitive', 'completed': False},
                {'player': 'bob', 'duration_minutes': 32, 'score': 1478,
                 'mode': 'casual', 'completed': True},
                {'player': 'diana', 'duration_minutes': 17, 'score': 1570,
                 'mode': 'competitive', 'completed': False},
                {'player': 'alice', 'duration_minutes': 98, 'score': 1981,
                 'mode': 'ranked', 'completed': True},
                {'player': 'diana', 'duration_minutes': 15, 'score': 2361,
                 'mode': 'competitive', 'completed': False},
                {'player': 'eve', 'duration_minutes': 29, 'score': 2985,
                 'mode': 'casual', 'completed': True},
                {'player': 'frank', 'duration_minutes': 34, 'score': 1285,
                 'mode': 'casual', 'completed': True},
                {'player': 'alice', 'duration_minutes': 53, 'score': 1238,
                 'mode': 'competitive', 'completed': False},
                {'player': 'bob', 'duration_minutes': 52, 'score': 1555,
                 'mode': 'casual', 'completed': False},
                {'player': 'frank', 'duration_minutes': 92, 'score': 2754,
                 'mode': 'casual', 'completed': True},
                {'player': 'eve', 'duration_minutes': 98, 'score': 1102,
                 'mode': 'casual', 'completed': False},
                {'player': 'diana', 'duration_minutes': 39, 'score': 2721,
                 'mode': 'ranked', 'completed': True},
                {'player': 'frank', 'duration_minutes': 46, 'score': 329,
                 'mode': 'casual', 'completed': True},
                {'player': 'charlie', 'duration_minutes': 56, 'score': 1196,
                 'mode': 'casual', 'completed': True},
                {'player': 'eve', 'duration_minutes': 117, 'score': 1388,
                 'mode': 'casual', 'completed': False},
                {'player': 'diana', 'duration_minutes': 118, 'score': 2733,
                 'mode': 'competitive', 'completed': True},
                {'player': 'charlie', 'duration_minutes': 22, 'score': 1110,
                 'mode': 'ranked', 'completed': False},
                {'player': 'frank', 'duration_minutes': 79, 'score': 1854,
                 'mode': 'ranked', 'completed': False},
                {'player': 'charlie', 'duration_minutes': 33, 'score': 666,
                 'mode': 'ranked', 'completed': False},
                {'player': 'alice', 'duration_minutes': 101, 'score': 292,
                 'mode': 'casual', 'completed': True},
                {'player': 'frank', 'duration_minutes': 25, 'score': 2887,
                 'mode': 'competitive', 'completed': True},
                {'player': 'diana', 'duration_minutes': 53, 'score': 2540,
                 'mode': 'competitive', 'completed': False},
                {'player': 'eve', 'duration_minutes': 115, 'score': 147,
                 'mode': 'ranked', 'completed': True},
                {'player': 'frank', 'duration_minutes': 118, 'score': 2299,
                 'mode': 'competitive', 'completed': False},
                {'player': 'alice', 'duration_minutes': 42, 'score': 1880,
                 'mode': 'casual', 'completed': False},
                {'player': 'alice', 'duration_minutes': 97, 'score': 1178,
                 'mode': 'ranked', 'completed': True},
                {'player': 'eve', 'duration_minutes': 18, 'score': 2661,
                 'mode': 'competitive', 'completed': True},
                {'player': 'bob', 'duration_minutes': 52, 'score': 761,
                 'mode': 'ranked', 'completed': True},
                {'player': 'eve', 'duration_minutes': 46, 'score': 2101,
                 'mode': 'casual', 'completed': True},
                {'player': 'charlie', 'duration_minutes': 117, 'score': 1359,
                 'mode': 'casual', 'completed': True}
                ],
            'game_modes': ['casual', 'competitive', 'ranked'],
            'achievements': ['first_blood', 'level_master', 'speed_runner',
                             'treasure_seeker', 'boss_hunter',
                             'pixel_perfect', 'combo_king', 'explorer']
            }
    print('\n=== List Comprehension Examples ===')
    high_scorers = [name for name in data['players']
                    if data['players'][name]['total_score'] > 2000]
    print(f'High scorers (>2000): {high_scorers}')
    scores_doubled = [player['total_score'] * 2 for player
                      in data['players'].values()]
    print(f'Scores doubled: {scores_doubled}')
    active_players = [name for name in data['players']
                      if data['players'][name]['sessions_played'] > 50]
    print(f'Active players: {active_players}')

    print('\n=== Dict Comprehension Examples ===')
    player_score = {player: score['total_score'] for player, score
                    in data['players'].items()}
    print(f'Player scores: {player_score}')
    score_categories = {
        'high': len({p: s['total_score'] for p, s in data['players'].items()
                     if s['total_score'] > 2000}),
        'medium': len({p: s['total_score'] for p, s in data['players'].items()
                       if 1500 <= s['total_score'] <= 2000}),
        'low': len({p: s['total_score'] for p, s in data['players'].items()
                    if s['total_score'] < 1500})
        }
    print(f'Score categories: {score_categories}')
    achievement_counts = {p: ac['achievements_count'] for p, ac
                          in data['players'].items()}
    print(f'Achievement counts: {achievement_counts}')

    print('\n=== Set Comprehension Examples ===')
    unique_players = {p['player'] for p in data['sessions']}
    print(f'Unique players: {unique_players}')
    unique_achievements = {a for a in data['achievements']}
    print(f'Unique achievements: {unique_achievements}')
    game_modes = {m for m in data['game_modes']}
    print(f'Game modes: {game_modes}')

    print('\n=== Combined Analysis ===')
    total_players = len([p for p in data['players']])
    print(f'Total players: {total_players}')
    print('Total unique achievements: ')
    total_unique_achievements = len({a for a in data['achievements']})
    print(f'Average score: {total_unique_achievements}')
    all_scores = [player['total_score'] for player in data['players'].values()]
    max_score = max(all_scores)
    name = [player for player, info in data['players'].items()
            if info['total_score'] == max_score][0]
    print(f'Top performer: {name} '
          f'({data["players"][name]['total_score']} points, '
          f'{data["players"][name]['achievements_count']} achievements)')


if __name__ == '__main__':
    try:
        main()
    except Exception as e:
        print(e)
