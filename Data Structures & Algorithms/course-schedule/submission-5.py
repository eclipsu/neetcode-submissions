class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:

        prereqs = collections.defaultdict(list)

        for course, prereq in prerequisites:
            print(course, prereq)
            prereqs[course].append(prereq)
        
        seen = set()
        def isCycle(course) -> bool:
            if course in seen:
                return True
            seen.add(course)

            for prereq in prereqs[course]:
                if isCycle(prereq):
                    return True

            prereqs[course] = []
            seen.remove(course)
            return False
        
        for num in range(numCourses):
            if isCycle(num):
                return False
        return True