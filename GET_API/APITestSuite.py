import unittest
import os
import FetchData
import ErrorData
import ComboData


# get all tests from FetchData class
fetch_data_test = unittest.TestLoader().loadTestsFromTestCase(FetchData.FetchData)
error_data_test = unittest.TestLoader().loadTestsFromTestCase(ErrorData.ErrorData)
combo_data_test = unittest.TestLoader().loadTestsFromTestCase(ComboData.ComboData)

# create a test suite combining search_text and home_page_test
test_suite = unittest.TestSuite([fetch_data_test, error_data_test,combo_data_test])

# get the directory path to output report file
#dir = os.getcwd()

# open the report file
#outfile = open(dir + "\APIPythonTestSummary.html", "w")

# configure HTMLTestRunner options
#runner = HtmlTestRunner.HtmlTestRunner(stream=outfile, title='Test Report', description='API Tests')
#runner.run(test_suite)

# run the suite using HTMLTestRunner
unittest.TextTestRunner(verbosity=2).run(test_suite)
