from importlib.metadata import version, PackageNotFoundError
try:
    import numpy as np
    import matplotlib.pyplot as plt
except ImportError:
    pass


def run_matrix_analysis(file_name: str) -> None:
    print('\nAnalyzing Matrix data...')

    data = np.random.randn(1000)
    plt.plot(data, color='green')
    plt.title("Matrix Signal Analysis")

    plt.savefig(file_name)
    print(f'Processing {len(data)} data points...')
    print('Generating visualization...')
    print(f'\nAnalysis complete!\nResults saved to: {file_name}')


def check_dependencies() -> None:

    packages = {
        'pandas': '2.1.0',
        'requests': '2.31.0',
        'matplotlib': '3.7.2'
    }
    all_ready = True
    print('\nChecking dependencies:')
    for pkg, vrs in packages.items():
        try:
            current_v = version(pkg)
            if current_v != vrs:
                print(f'[Warning] {pkg} ({vrs}) - Package found but wrong version')
            else:
                print(f'[OK] {pkg} ({vrs}) - Ready to be used')
        except PackageNotFoundError:
            print(f'[KO] {pkg} not found')
            all_ready = False
    if not all_ready:
        print('\nPlease run "pip install -r requirements.txt"'
                ' to install all the missing packages')
    else:
        try:
            run_matrix_analysis('matrix_analysis.png')
        except Exception as e:
            print(f"Error during analysis: {e}")

if __name__ == '__main__':
    print('\nLOADING STATUS: Loading programs...')
    check_dependencies()
