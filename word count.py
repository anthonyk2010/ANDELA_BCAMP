def test_count_one_of_each(self):
        self.assertEqual(
            {'olly': 2, 'in': 1, 'come': 1,'free' :1},
            word_count('olly olly in come free"')
