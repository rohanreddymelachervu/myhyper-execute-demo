def pytest_addoption(parser):
    parser.addoption(
        "--browser",
        action="store",
        default="Chrome",
        help="Browser to run tests on (Chrome or Firefox)"
    )
    parser.addoption(
        "--os",
        action="store",
        default="Windows 10",
        help="Operating system for tests (e.g., Windows 10, Windows 11, Linux)"
    )
