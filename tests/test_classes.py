from lib.classes import *

def test_reminds_the_user_to_do_a_task():
    reminder = Reminder("Kay")
    reminder.remind_me_to("Walk the dog")
    result = reminder.remind()
    assert result == "Walk the dog, Kay!"

# We would typically have a number of these examples.

def test_is_counter_an_instance_of_Counter():
    count_obj = Counter()
    assert  isinstance(count_obj, Counter) == True

def test_add_and_report_count_object():
    count_obj1 = Counter()
    count_obj1.add(1)
    assert count_obj1.report() == "Counted to 1 so far."

def test_multiple_add_calls_on_Counter_object():
    count_obj2 = Counter()
    count_obj2.add(5)
    count_obj2.add(50)
    count_obj2.add(5000)
    assert count_obj2.report() == "Counted to 5055 so far."

def test_Stringbuiler_size():
    str_builder_1 = StringBuilder()
    str_builder_1.add("Hello world")
    assert str_builder_1.size() == 11

def test_Stringbuiler_output():
    str_builder2 = StringBuilder()
    str_builder2.add("Bob the developer, can he break it?")
    assert str_builder2.output() == "Bob the developer, can he break it?"

def test_Stringbuiler_multiple_add_calls():
    str_builder3 = StringBuilder()
    str_builder3.add("one")
    str_builder3.add(" two")
    str_builder3.add(" three")
    assert str_builder3.output() == "one two three"

def test_Gratitude_methods_add_format():
    gratitude_single_list = Gratitudes()
    gratitude_single_list.add("almond croissants")
    assert gratitude_single_list.format() == "Be grateful for: almond croissants"

    gratitude_multiple_list = Gratitudes()
    gratitude_multiple_list.add("carrot cake")
    gratitude_multiple_list.add("chilli sauce")
    gratitude_multiple_list.add("yum yums")
    assert gratitude_multiple_list.format() == "Be grateful for: carrot cake, chilli sauce, yum yums"