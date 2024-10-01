import pandas as pd
import os
from main.models import Teams, TeamTypes, Posts, AgeGroups
from django.utils.text import slugify
from datetime import datetime

# current_dir = os.path.dirname(__file__)

# # Replace with the path to your CSV file
# csv_file_path = os.path.join(current_dir, 'teams.csv')

# # Read the CSV file into a DataFrame
# df = pd.read_csv(csv_file_path)

# Loop through the DataFrame and create instances of the models
# for index, row in df.iterrows():
#     # # Get or create TeamTypes
#     # team_type_instances = []
#     # if pd.notna(row['teamTypes']):
#     #     team_types = row['teamTypes'].strip('"').split(',')  # Handle multiple entries
#     #     for type_name in team_types:
#     #         team_type, created = TeamTypes.objects.get_or_create(types=type_name.strip())
#     #         team_type_instances.append(team_type)

#     # # Get or create Posts
#     # post_instances = []
#     # if pd.notna(row['posts']):
#     #     post_titles = row['posts'].strip('"').split(',')  # Handle multiple entries
#     #     for title in post_titles:
#     #         post, created = Posts.objects.get_or_create(post=title.strip())
#     #         post_instances.append(post)

#     # # Get or create AgeGroups
#     # agegroup_instances = []
#     # if pd.notna(row['agegroups']):
#     #     agegroup_names = row['agegroups'].strip('"').split(',')  # Handle multiple entries
#     #     for agegroup_name in agegroup_names:
#     #         agegroup, created = AgeGroups.objects.get_or_create(name=agegroup_name.strip())
#     #         agegroup_instances.append(agegroup)

#     # Create or update Teams
#     team, created = Teams.objects.get_or_create(
#         name=row['name'],
#         defaults={
#             'city': row.get('city', ''),
#             'state': row.get('state', ''),
#             'contactName': row.get('contactName', ''),
#             'contactEmail': row.get('contactEmail', ''),
#             'contactPhone': row.get('contactPhone', ''),
#             'website': row.get('website', ''),
#             'slug': slugify(row['name']),
#             'dateAdded': datetime.now(),
#         }
#     )

#     # Add the ManyToMany fields
#     # if team_type_instances:
#     #     team.teamTypes.set(team_type_instances)
#     # if post_instances:
#     #     team.posts.set(post_instances)
#     # if agegroup_instances:
#     #     team.agegroups.set(agegroup_instances)

#     # Save the team instance
#     team.save()
