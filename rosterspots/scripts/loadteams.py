import pandas as pd
from django.utils.text import slugify
from main.models import Posts, TeamTypes, Ages, Teams

# Load Excel data into a pandas DataFrame
df = pd.read_excel('teams.xlsx')

# Loop through each row in the DataFrame and create model instances
for index, row in df.iterrows():
    # Create or get Posts instances and add them to the team
    post_objs = []
    for post in row['posts'].split(','):
        post_obj, created = Posts.objects.get_or_create(post=post.strip())
        post_objs.append(post_obj)
    
    # Create or get TeamTypes instances and add them to the team
    team_type_objs = []
    for team_type in row['teamTypes'].split(','):
        team_type_obj, created = TeamTypes.objects.get_or_create(types=team_type.strip())
        team_type_objs.append(team_type_obj)
    
    # Create or get Ages instances and add them to the team
    age_objs = []
    for age in row['ages'].split(','):
        age_obj, created = Ages.objects.get_or_create(ages=age.strip())
        age_objs.append(age_obj)
    
    # Create the Teams instance
    team = Teams.objects.create(
        name=row['name'],
        city=row['city'],
        state=row['state'],
        contactName=row['contactName'],
        contactEmail=row['contactEmail'],
        contactPhone=row['contactPhone'],
        website=row['website'],
        image=row['image'],
        picture=row['picture'],
        instagramUser=row['instagramUser'],
        xUser=row['xUser'],
        slug=slugify(row['name']),
        dateAdded=row['dateAdded']
    )
    
    # Add the many-to-many relationships
    team.posts.set(post_objs)
    team.teamTypes.set(team_type_objs)
    team.Ages.set(age_objs)
    
    # Save the team instance
    team.save()

print("Records have been inserted successfully.")
