from lib.diary import Diary
from lib.diary_entry import DiaryEntry

"""
adds two diary entries
returned in list
"""
def test_add_and_return_list():   
    diary = Diary()
    entry_1 = DiaryEntry("My Title", "some contents")
    entry_2 = DiaryEntry("This Title", "some other contents")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.all() == [entry_1, entry_2]

"""
Given 2 diary entries
call count_words
returns all words in content of diary entries
"""
def test_count_words_returns_count_for_all_entry_content():
    diary = Diary()
    entry_1 = DiaryEntry("My Title", "one two")
    entry_2 = DiaryEntry("This Title", "three four five")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.count_words() == 5

"""
Given add two diary entries with total length of 5
reading_time with wpm of 2
total reading time should be 3
"""
def test_reading_time_returns_time_to_read_all_entries():
    diary = Diary()
    entry_1 = DiaryEntry("My Title", "one two")
    entry_2 = DiaryEntry("This Title", "three four five")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.reading_time(2) == 3

"""
Given add two entries, one long and one short
call find_best_entry_for_reading_time
with wpm and minutes so i can only read short entry
Find_best_entry_for_reading_time should return shorter entry
"""

def test_find_best_entry_for_reading_time_returns_short_entry():
    diary = Diary()
    entry_1 = DiaryEntry("My Title", "one two three")
    entry_2 = DiaryEntry("This Title", "three four five six seven")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2, 2) == entry_1

"""
Given add entry
call find_best_entry_for_reading_time
with wpm and minutes so i can read entry 
find_best_entry_for_reading_time returns entry
"""

def test_find_best_entry_for_reading_time_returns_entry():
    diary = Diary()
    entry_1 = DiaryEntry("My Title", "one two three")
    diary.add(entry_1)
    assert diary.find_best_entry_for_reading_time(2, 3) == entry_1

"""
Given add entry
call find_best_entry_for_reading_time
with wpm and minutes so i cannot read entry 
find_best_entry_for_reading_time returns none
"""
def test_find_best_reading_time_returns_none_when_none_readable():
    diary = Diary()
    entry_1 = DiaryEntry("My Title", "one two three four five six seven")
    diary.add(entry_1)
    assert diary.find_best_entry_for_reading_time(2, 3) == None

"""
Given add entries of equal length
call find_best_entry_for_reading_time
with wpm and minutes so i could read both 
find_best_entry_for_reading_time returns longer entry
"""

def test_find_reading_time_for_time_returns_longest_readable():
    diary = Diary()
    entry_1 = DiaryEntry("My Title", "one two three")
    entry_2 = DiaryEntry("This Title", "one two three four five six seven")
    diary.add(entry_1)
    diary.add(entry_2)
    assert diary.find_best_entry_for_reading_time(2, 4) == entry_2