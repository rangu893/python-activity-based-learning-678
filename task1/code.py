class ScholarshipSystem:
    def __init__(self, min_aggregate=85.0, min_subject_score=70, min_attendance=80.0, max_income=50000):
        self.min_aggregate = min_aggregate
        self.min_subject_score = min_subject_score
        self.min_attendance = min_attendance
        self.max_income = max_income
        self.eligible_applicants = []
        self.rejected_applicants = []

    def evaluate_applicants(self, applicants):
        for app in applicants:
            reasons = []
            
            # Check criteria
            if app['aggregate'] < self.min_aggregate:
                reasons.append(f"Aggregate {app['aggregate']}% below {self.min_aggregate}%")
            
            failed_subjects = [sub for sub, score in app['subjects'].items() if score < self.min_subject_score]
            if failed_subjects:
                reasons.append(f"Subject score below {self.min_subject_score} in: {', '.join(failed_subjects)}")
                
            if app['attendance'] < self.min_attendance:
                reasons.append(f"Attendance {app['attendance']}% below {self.min_attendance}%")
                
            if app['income'] > self.max_income:
                reasons.append(f"Income ${app['income']} exceeds max limit ${self.max_income}")

            if not reasons:
                self.eligible_applicants.append(app)
            else:
                app['reasons'] = "; ".join(reasons)
                self.rejected_applicants.append(app)

    def rank_applicants(self):
        # Sort by: Aggregate DESC, Income ASC, Attendance DESC
        self.eligible_applicants.sort(
            key=lambda x: (-x['aggregate'], x['income'], -x['attendance'])
        )
        
        # Assign ranks
        for rank, app in enumerate(self.eligible_applicants, start=1):
            app['rank'] = rank

    def display_results(self):
        print("=== SCHOLARSHIP ALLOCATION RESULTS ===")
        print(f"\n[ELIGIBLE & RANKED STUDENTS ({len(self.eligible_applicants)})]")
        print(f"{'Rank':<6}{'Name':<15}{'Aggregate':<12}{'Income':<10}{'Attendance'}")
        print("-" * 55)
        for app in self.eligible_applicants:
            print(f"{app['rank']:<6}{app['name']:<15}{app['aggregate']:<12.1f}${app['income']:<9}{app['attendance']}%")

        print(f"\n[REJECTED APPLICANTS ({len(self.rejected_applicants)})]")
        print(f"{'Name':<15}{'Reason for Rejection'}")
        print("-" * 55)
        for app in self.rejected_applicants:
            print(f"{app['name']:<15}{app['reasons']}")


# --- Sample Execution ---
if __name__ == "__main__":
    # Sample Input Data
    applicants_data = [
        {"name": "Alice Smith", "aggregate": 91.5, "subjects": {"Math": 85, "Physics": 88, "Chemistry": 90}, "attendance": 92.0, "income": 42000},
        {"name": "Bob Jones", "aggregate": 88.0, "subjects": {"Math": 72, "Physics": 75, "Chemistry": 80}, "attendance": 85.0, "income": 35000},
        {"name": "Charlie Brown", "aggregate": 91.5, "subjects": {"Math": 90, "Physics": 92, "Chemistry": 89}, "attendance": 95.0, "income": 38000}, # Tie with Alice on aggregate, lower income -> higher rank
        {"name": "Diana Prince", "aggregate": 84.0, "subjects": {"Math": 80, "Physics": 85, "Chemistry": 82}, "attendance": 90.0, "income": 25000}, # Failed aggregate
        {"name": "Evan Wright", "aggregate": 89.0, "subjects": {"Math": 65, "Physics": 80, "Chemistry": 85}, "attendance": 88.0, "income": 40000}, # Failed subject math
        {"name": "Fiona Gallagher", "aggregate": 93.0, "subjects": {"Math": 95, "Physics": 94, "Chemistry": 96}, "attendance": 96.0, "income": 48000}
    ]

    system = ScholarshipSystem()
    system.evaluate_applicants(applicants_data)
    system.rank_applicants()
    system.display_results()
