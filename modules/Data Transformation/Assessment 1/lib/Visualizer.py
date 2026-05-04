import matplotlib.pyplot as plt

class Visualizer:
    '''
    This class visualizes the dataset using matplotlib.
    '''

    def __init__(self, df):
        self.df = df


    def VisualizeWaitTimeDistributionOverall(self):
        plt.figure()
        plt.hist(self.df["Wait Time Days"], bins=20)
        plt.title("Wait Times Distribution Overall")
        plt.figtext(
            x=0.2,
            y=0.5,
            s= """ 
            This chart presents the wait time distribution overall. It provides a
            big-picture overview of staff availability and may prove useful to 
            health board management in onboarding new staff.
            """,
            )
        plt.xlabel("Wait Time (days)")
        plt.ylabel("Number of Appointments")
        plt.show()

    def VisualizeWaitTimeDistributionByBoard(self):

        boards = self.df["Health Board"].unique()

        for board in boards:
            plt.figure()
            subset = self.df[self.df["Health Board"] == board]

            plt.hist(subset["Wait Time Days"], bins=20, alpha=0.5, label=board)

            plt.title(f"Wait Time Distribution in {board}")
            plt.figtext(
            x=0.2,
            y=0.5,
            s= """ 
            This chart is a more fine-grained version of the previous one. It breaks
            down wait time distribution by each unique health board. It provides a
            big-picture overview of staff availability in each health board, allowing
            management to reallocate existing staff in accordance with the demand.

            To increase readability and prevent overlapping records, each health board
            is shown separately.
            """,
            )
            plt.xlabel("Wait Time (days)")
            plt.ylabel("Number of Appointments")
            plt.legend()

            plt.show()

    def VisualizeDnaRatesBySpecialty(self):
        specialties = self.df["Specialty"].unique() # Get all specialties

        plt.figure()

        for specialty in specialties: 
            #subset = self.df[self.df["Specialty"] == specialty] # 
#
            #subset = subset[subset["Outcome"] == "DNA"]
            dna_counts = self.df[self.df["Outcome"] == "DNA"]["Specialty"].value_counts()
            plt.bar(dna_counts.index, dna_counts.values)

        plt.title("DNA (did not attend) Rates by Specialty")
        plt.figtext(
            x=0.2,
            y=0.5,
            s= """ 
            This chart presents the number of DNA records by each unique specialty.
            It may help health service identify which specialty sees the least
            patients, and develop a solution to the problem - e.g. Fees for
            not attending an appointment with a specialty who gets the most DNAs.
            """,
            )
        plt.xlabel("Specialty")
        plt.xticks(rotation=90)
        plt.ylabel("Number of DNAs")
        plt.show()

    def VisualizeSatisfactionScoreDistributionBySpecialty(self):
        specialties = self.df["Specialty"].unique()

        for specialty in specialties:
            plt.figure()
            subset = self.df[self.df["Specialty"] == specialty] # grab all records of specialty
            subset = subset[subset["Satisfaction Score"] != 0] # prune records where satisfaction score == 0

            plt.hist(subset["Satisfaction Score"], bins=20, alpha=0.5, label=specialty)
            plt.figtext(
            x=0.2,
            y=0.5,
            s= """ 
            This chart shows the satisfaction score distribution by each unique specialty.
            To avoid overlapping bars and vastly increase readability, each specialty is
            presented separately. This visualization may help health service identify
            specialties who fail to meet patient's needs, and conversly, those who do it very 
            well. This could lead to actions such as reallocation of resources to the
            specialties who need them most.
            """,
            )

            plt.title("Satisfaction Score by Specialty")
            plt.xlabel("Satisfaction Score")
            plt.ylabel("Number of Occurences")
            plt.legend()
            plt.show()

    
    def VisualiseRelationshipBetweenWaitTimeAndConsultationDuration(self):

        filtered = self.df[
            (self.df["Wait Time Days"] != 0) &
            (self.df["Duration Minutes"] != 0)
        ]
        plt.figure()
        plt.scatter(filtered["Wait Time Days"], filtered["Duration Minutes"])
        
        plt.title("Corelation Between Wait Time (days) and Appointment Duration (minutes)")
        plt.figtext(
            x=0.2,
            y=0.5,
            s= """ 
            This chart shows the corelation between wait time and appointment duration.
            Each dot represents a unique record. It matters because it could reveal important trends
            in corelation between longer wait times and appointment duration.
            The chart shows that no such corelation exists. Appoinment duration is not corelated to the
            wait time at all.""",
        )
        plt.xlabel("Wait Time (days)")
        plt.ylabel("Appointment Duration (minutes)")
        plt.show()