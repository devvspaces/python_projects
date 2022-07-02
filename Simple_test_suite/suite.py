"""
A Simple test suite to for running tests
"""


class MyTestSuite:
    def __init__(self, name='') -> None:
        self._test_count = 0
        self._passed = []
        self._failed = []
        self._name = name

    def get_passed(self):
        """
        Returns only passed results
        """
        for result in self._passed:
            print(result)

        print(f'\n{len(self._passed)} tests passed')

    def get_fails(self):
        """
        Returns only failed results
        """
        for result in self._failed:
            print(result)

        print(f'\n{len(self._failed)} tests failed')

    def get_merge_result(self):
        """
        Returns a merge of passed and failed tests
        """
        return self._passed + self._failed

    def get_results(self):
        """
        Returns all passed and failed results
        """
        results = self.get_merge_result()
        for result in results:
            print(result)

        print(f'Ran {len(results)} tests. {len(self._passed)} passed and {len(self._failed)} failed')  # noqa

    def fetch_results(self):
        """
        Returns all passed and failed results
        """
        results = self.get_merge_result()

        print('>'*10, 'Tests Results', '\n')
        print("="*10, 'Passed Tests', "="*10)
        self.get_passed()
        print('\n')

        print("="*10, 'Failed Tests', "="*10)
        self.get_fails()
        print('\n')

        print('_'*40)
        print(f'| Ran {len(results)} tests. {len(self._passed)} passed and {len(self._failed)} failed |')  # noqa
        print('='*40)

    def run_test(self, computed, expected, label: str = ""):
        """
        Checks the computed result against the expected
        Saves a message in failed or passed
        """
        if not label:
            self._test_count += 1
            label = f"#{self._test_count}"

        if computed == expected:
            message = f"Test {label}: Computed: {computed} Expected: {expected}"  # noqa
            self._passed.append(message)
        else:
            message = f"Test {label}: Computed: {computed} Expected: {expected}"  # noqa
            self._failed.append(message)

    def __str__(self) -> str:
        if self._name:
            return self._name
        return 'TestSuite'


if __name__ == '__main__':

    def run_test():
        """
        Running a demo test if module ran
        """
        suite = MyTestSuite('Unique Test suite')

        suite.run_test(2, 1)
        suite.run_test(2, 2)
        suite.run_test(2, 2)
        suite.run_test(2, 2)
        suite.run_test(2, 4)
        suite.run_test(2, 2)
        suite.run_test(2, 0)
        suite.run_test(2, 2)

        suite.fetch_results()

    run_test()
