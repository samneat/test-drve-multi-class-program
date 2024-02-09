from lib.diary_entry import DiaryEntry

"""
When initialise with title and content
title and content can be returned
"""

def test_construct_and_get_title_and_content():
    diary_entry = DiaryEntry("My Title", "Some contents")
    assert diary_entry.title == "My Title"
    assert diary_entry.contents == "Some contents"

"""
When initialised with 5 word content
count_words should return 5
"""
def test_count_words_returns_count_of_contents():
    diary_entry = DiaryEntry("My Title", "one two three four five")
    assert diary_entry.count_words() == 5

"""
initialise with five word content
reading_time wit wpm of 2 should return 3
"""

def test_reading_time():
    diary_entry = DiaryEntry("My Title", "one two three four five")
    assert diary_entry.reading_time(2) == 3

"""
when initialise with 5 word content
first reading_chunk should return the first chunk readable in the time
"""

def test_readable_chunk_first_chunk():
    diary_entry = DiaryEntry("My Title", "one two three four five")
    assert diary_entry.reading_chunk(2, 1) == "one two"


"""
when initialise with 5 word content
second reading_chunk should return the second chunk readable in the time
"""

def test_readable_chunk_second_chunk():
    diary_entry = DiaryEntry("My Title", "one two three four five")
    diary_entry.reading_chunk(2, 1)
    assert diary_entry.reading_chunk(2, 1) == "three four"

"""
when i initialise with 5 word content
on third call reading_chunk should return final partial chunk
"""
def test_readable_chunk_third_chunk():
    diary_entry = DiaryEntry("My Title", "one two three four five")
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1)
    assert diary_entry.reading_chunk(2, 1) == "five"

"""
when i initialise with 5 word content
on fourth call reading_chunk should start from beginning
"""

def test_readable_chunk_fourth_chunk():
    diary_entry = DiaryEntry("My Title", "one two three four five")
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1)
    assert diary_entry.reading_chunk(2, 1) == "one two"

    """
when i initialise with 6 word content
on fourth call reading_chunk should start from beginning
"""

def test_readable_chunk_fourth_chunk_with_exact_chunks():
    diary_entry = DiaryEntry("My Title", "one two three four five")
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1)
    diary_entry.reading_chunk(2, 1)
    assert diary_entry.reading_chunk(2, 1) == "one two"