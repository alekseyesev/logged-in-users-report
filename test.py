from io import StringIO
import unittest
from mock_events import events
from utils import current_users, generate_report


class TestApp(unittest.TestCase):
    def setUp(self):
        self.users = current_users(events)

    def test_current_users(self):
        self.assertEqual(self.users, {"myworkstation.local": set(
        ), "webserver.local": {"jordan", "lane"}, "mailserver.local": {"chris"}})

    def test_generate_report(self):
        output = StringIO()

        generate_report(self.users, output)

        report = output.getvalue()

        output.close()

        self.assertIn(
            report, ["webserver.local: lane, jordan\n" + "mailserver.local: chris\n", "webserver.local: jordan, lane\n" + "mailserver.local: chris\n"])


if __name__ == "__main__":
    unittest.main()
