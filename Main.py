
from pyscript import document

# ICT Club members
grade_7 = {'Samantha Jose', 'Maria Santos'}
grade_8 = {'John Smith', 'Alex Cruz'}
grade_9 = {'Patricia Star', 'James Lee'}
grade_10 = {'Nick Gurt', 'Sofia Reyes'}

# members
new_members = set()


def add_member(event):
    first_name = document.getElementById('first-name').value.strip()
    last_name = document.getElementById('last-name').value.strip()

    full_name = f'{first_name} {last_name}'.strip()

    new_members.add(full_name)

    # Combine all member sets
    members = grade_7 | grade_8 | grade_9 | grade_10 | new_members

    # Display the results
    document.getElementById('output').innerHTML = (
        f'Member Added: {full_name}<br><br>'
        f'Total Members: {len(members)}'
    )
