import unittest

from katas.kyu_4.a_simplistic_tcp_finite_state_machine import \
    traverse_tcp_states


class TraverseTCPStatesTestCase(unittest.TestCase):
    def test_traverse_tcp_states(self):
        self.assertEqual(traverse_tcp_states(["APP_ACTIVE_OPEN", "RCV_SYN_ACK", "RCV_FIN"]), "CLOSE_WAIT")
        self.assertEqual(traverse_tcp_states(["APP_PASSIVE_OPEN", "RCV_SYN", "RCV_ACK"]), "ESTABLISHED")
        self.assertEqual(traverse_tcp_states(["APP_ACTIVE_OPEN", "RCV_SYN_ACK", "RCV_FIN", "APP_CLOSE"]), "LAST_ACK")
        self.assertEqual(traverse_tcp_states(["APP_ACTIVE_OPEN"]), "SYN_SENT")
        self.assertEqual(traverse_tcp_states([]), "CLOSED")
        self.assertEqual(traverse_tcp_states(["APP_PASSIVE_OPEN", "RCV_SYN", "RCV_ACK", "APP_CLOSE", "APP_SEND"]),
                         "ERROR")
