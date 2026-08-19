class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        prereqs = collections.defaultdict(list)

        for course, prereq in prerequisites:
            prereqs[course].append(prereq)
        
        seen = set()

        def hasCycle(course) -> bool:
            if course in seen:
                return True
            
            seen.add(course)

            for prereq in prereqs[course]:
                if hasCycle(prereq):
                    return True
            
            prereqs[course] = []
            seen.remove(course)
            return False
        
        for num in range(numCourses):
            if hasCycle(num):
                return False
        return True
