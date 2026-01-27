from sys import argv as av

def ft_score_analytics() -> None:
    ac = len(av)
    if ac < 2:
        print('No scores provided. Usage: python3 ft_score_analytics.py <score1> <score2> ...')
    else:
        scores: list[int] = []
        for i in range(1, ac):
            try:
                score = int(av[i])
                scores.append(score)
            except ValueError as e:
                print(e)
                scores = []
        num_players = ac - 1
        total = sum(scores)
        min_score = min(scores)
        max_score = max(scores)
        print(f'Scores processed: {scores}')
        print(f'Total players: {num_players}')
        print(f'Total score: {total}')
        print(f'Average score: {total / num_players}')
        print(f'High score: {max_score}')
        print(f'Low score: {min_score}')
        print(f'Score range: {max_score - min_score}')


if __name__ == '__main__':
    try:
        print('=== Player Score Analytics ===')
        ft_score_analytics()
    except Exception as e:
        print(e)
