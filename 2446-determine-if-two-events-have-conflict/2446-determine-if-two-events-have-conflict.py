class Solution:
    def haveConflict(self, event1: List[str], event2: List[str]) -> bool:
        def convert_to_minutes(time_str):
            hours, minutes = map(int, time_str.split(":"))
            return hours * 60 + minutes

        start_time1, end_time1 = event1
        start_time2, end_time2 = event2

        start_minutes1 = convert_to_minutes(start_time1)
        end_minutes1 = convert_to_minutes(end_time1)
        start_minutes2 = convert_to_minutes(start_time2)
        end_minutes2 = convert_to_minutes(end_time2)

        # Check for non-empty intersection
        if start_minutes1 <= end_minutes2 and start_minutes2 <= end_minutes1:
            return True
        else:
            return False
            