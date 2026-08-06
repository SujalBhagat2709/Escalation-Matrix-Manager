"""
Escalation Matrix Studio
------------------------
Main file for Escalation Matrix Manager.
"""

from escalation_matrix_manager import EscalationMatrixManager


class EscalationMatrixStudio:

    def __init__(self):

        self.manager = EscalationMatrixManager()

    # ----------------------------------
    # Add Ticket
    # ----------------------------------
    def add_ticket(self):

        print("\n========== ADD TICKET ==========\n")

        ticket = self.manager.add_ticket(

            input("Ticket ID: ").strip(),

            input("Issue: ").strip(),

            input("Owner: ").strip(),

            int(
                input(
                    "Escalation Level (1-3): "
                )
            )

        )

        if ticket:

            print("\nTicket Added Successfully.")

            self.manager.display_ticket(ticket)

        else:

            print("\nTicket ID already exists.")

    # ----------------------------------
    # Escalate Ticket
    # ----------------------------------
    def escalate_ticket(self):

        ticket_id = input(
            "\nTicket ID: "
        ).strip()

        if self.manager.escalate_ticket(
            ticket_id
        ):

            print("\nTicket escalated successfully.")

        else:

            print(
                "\nUnable to escalate ticket."
            )

    # ----------------------------------
    # Resolve Ticket
    # ----------------------------------
    def resolve_ticket(self):

        ticket_id = input(
            "\nTicket ID: "
        ).strip()

        if self.manager.resolve_ticket(
            ticket_id
        ):

            print("\nTicket resolved successfully.")

        else:

            print("\nTicket not found.")

    # ----------------------------------
    # Search Ticket
    # ----------------------------------
    def search_ticket(self):

        keyword = input(
            "\nSearch Issue / Owner: "
        ).strip()

        results = self.manager.search_ticket(
            keyword
        )

        if not results:

            print("\nNo matching tickets found.")

            return

        for ticket in results:

            self.manager.display_ticket(
                ticket
            )

    # ----------------------------------
    # View Tickets
    # ----------------------------------
    def view_tickets(self):

        self.manager.display_tickets()

    # ----------------------------------
    # Statistics
    # ----------------------------------
    def statistics(self):

        self.manager.display_statistics()

    # ----------------------------------
    # Summary
    # ----------------------------------
    def summary(self):

        self.manager.display_summary()

    # ----------------------------------
    # Menu
    # ----------------------------------
    def menu(self):

        while True:

            print("\n" + "=" * 60)
            print("        ESCALATION MATRIX MANAGER")
            print("=" * 60)

            print("1. Add Ticket")
            print("2. Escalate Ticket")
            print("3. Resolve Ticket")
            print("4. View Tickets")
            print("5. Search Ticket")
            print("6. Escalation Statistics")
            print("7. Summary")
            print("8. Exit")

            choice = input(
                "\nEnter Choice: "
            ).strip()

            if choice == "1":

                self.add_ticket()

            elif choice == "2":

                self.escalate_ticket()

            elif choice == "3":

                self.resolve_ticket()

            elif choice == "4":

                self.view_tickets()

            elif choice == "5":

                self.search_ticket()

            elif choice == "6":

                self.statistics()

            elif choice == "7":

                self.summary()

            elif choice == "8":

                print(
                    "\nThank you for using Escalation Matrix Manager."
                )

                break

            else:

                print("\nInvalid choice.")


# ----------------------------------
# Main
# ----------------------------------

if __name__ == "__main__":

    studio = EscalationMatrixStudio()

    studio.menu()