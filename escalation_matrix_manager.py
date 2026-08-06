"""
Escalation Matrix Manager
-------------------------
File : escalation_matrix_manager.py

Features
--------
✔ Add Escalation Rule
✔ Escalate Ticket
✔ Resolve Ticket
✔ Search Ticket
✔ Pending Escalations
✔ Resolved Escalations
✔ Escalation Level Statistics
✔ Summary Report
"""


class EscalationMatrixManager:

    def __init__(self):

        self.tickets = []

    # ----------------------------------
    # Ticket Exists
    # ----------------------------------
    def ticket_exists(self,
                      ticket_id):

        for ticket in self.tickets:

            if ticket["Ticket ID"] == ticket_id:

                return True

        return False

    # ----------------------------------
    # Add Ticket
    # ----------------------------------
    def add_ticket(self,
                   ticket_id,
                   issue,
                   owner,
                   level):

        if self.ticket_exists(ticket_id):

            return None

        ticket = {

            "Ticket ID": ticket_id,
            "Issue": issue,
            "Owner": owner,
            "Escalation Level": level,
            "Status": "Open"

        }

        self.tickets.append(ticket)

        return ticket

    # ----------------------------------
    # Escalate Ticket
    # ----------------------------------
    def escalate_ticket(self,
                        ticket_id):

        for ticket in self.tickets:

            if ticket["Ticket ID"] == ticket_id:

                if ticket["Status"] == "Resolved":

                    return False

                if ticket["Escalation Level"] < 3:

                    ticket["Escalation Level"] += 1

                return True

        return False

    # ----------------------------------
    # Resolve Ticket
    # ----------------------------------
    def resolve_ticket(self,
                       ticket_id):

        for ticket in self.tickets:

            if ticket["Ticket ID"] == ticket_id:

                ticket["Status"] = "Resolved"

                return True

        return False

    # ----------------------------------
    # Search Ticket
    # ----------------------------------
    def search_ticket(self,
                      keyword):

        keyword = keyword.lower()

        return [

            ticket

            for ticket in self.tickets

            if keyword in
            ticket["Issue"].lower()

            or keyword in
            ticket["Owner"].lower()

        ]

    # ----------------------------------
    # Pending Tickets
    # ----------------------------------
    def pending_tickets(self):

        return [

            ticket

            for ticket in self.tickets

            if ticket["Status"] == "Open"

        ]

    # ----------------------------------
    # Resolved Tickets
    # ----------------------------------
    def resolved_tickets(self):

        return [

            ticket

            for ticket in self.tickets

            if ticket["Status"] == "Resolved"

        ]

    # ----------------------------------
    # Escalation Statistics
    # ----------------------------------
    def level_statistics(self):

        stats = {

            1: 0,
            2: 0,
            3: 0

        }

        for ticket in self.tickets:

            stats[
                ticket["Escalation Level"]
            ] += 1

        return stats

    # ----------------------------------
    # Summary
    # ----------------------------------
    def summary(self):

        return {

            "Total Tickets":
                len(self.tickets),

            "Pending":
                len(
                    self.pending_tickets()
                ),

            "Resolved":
                len(
                    self.resolved_tickets()
                )

        }

    # ----------------------------------
    # Display Ticket
    # ----------------------------------
    def display_ticket(self,
                       ticket):

        print("\n========== TICKET ==========\n")

        for key, value in ticket.items():

            print(f"{key:<20}: {value}")

    # ----------------------------------
    # Display All Tickets
    # ----------------------------------
    def display_tickets(self):

        if not self.tickets:

            print("\nNo tickets available.")

            return

        print("\n========== ESCALATION REPORT ==========\n")

        for index, ticket in enumerate(

                self.tickets,
                start=1):

            print(f"Ticket {index}")

            print("-" * 40)

            for key, value in ticket.items():

                print(f"{key:<20}: {value}")

            print()

    # ----------------------------------
    # Display Statistics
    # ----------------------------------
    def display_statistics(self):

        stats = self.level_statistics()

        print("\n========== LEVEL STATISTICS ==========\n")

        for level, count in stats.items():

            print(f"Level {level:<13}: {count}")

    # ----------------------------------
    # Display Summary
    # ----------------------------------
    def display_summary(self):

        report = self.summary()

        print("\n========== SUMMARY ==========\n")

        for key, value in report.items():

            print(f"{key:<20}: {value}")


# ----------------------------------
# Example
# ----------------------------------

if __name__ == "__main__":

    manager = EscalationMatrixManager()

    while True:

        print("\n1. Add Ticket")
        print("2. Escalate Ticket")
        print("3. Resolve Ticket")
        print("4. View Tickets")
        print("5. Search Ticket")
        print("6. Level Statistics")
        print("7. Summary")
        print("8. Exit")

        choice = input("\nEnter Choice: ")

        if choice == "1":

            ticket = manager.add_ticket(

                input("Ticket ID: "),

                input("Issue: "),

                input("Owner: "),

                int(
                    input(
                        "Escalation Level (1-3): "
                    )
                )

            )

            if ticket:

                manager.display_ticket(ticket)

            else:

                print("\nTicket ID already exists.")

        elif choice == "2":

            if manager.escalate_ticket(

                input("Ticket ID: ")

            ):

                print("\nTicket escalated.")

            else:

                print("\nUnable to escalate ticket.")

        elif choice == "3":

            if manager.resolve_ticket(

                input("Ticket ID: ")

            ):

                print("\nTicket resolved.")

            else:

                print("\nTicket not found.")

        elif choice == "4":

            manager.display_tickets()

        elif choice == "5":

            keyword = input("Search: ")

            results = manager.search_ticket(
                keyword
            )

            if results:

                for ticket in results:

                    manager.display_ticket(
                        ticket
                    )

            else:

                print("\nNo matching tickets found.")

        elif choice == "6":

            manager.display_statistics()

        elif choice == "7":

            manager.display_summary()

        elif choice == "8":

            print(
                "\nThank you for using Escalation Matrix Manager."
            )

            break

        else:

            print("\nInvalid choice.")