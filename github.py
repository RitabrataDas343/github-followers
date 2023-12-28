import requests

def get_github_users(api_url, token):
    users = []

    headers = {'Authorization': f'token {token}'}

    while api_url:
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            users.extend(response.json())
            api_url = response.links.get('next', {}).get('url')
        else:
            print(f"Error: {response.status_code}, {response.text}")
            break

    return [user['login'] for user in users]

def get_github_followers_and_following(username, token):
    followers_url = f'https://api.github.com/users/{username}/followers'
    following_url = f'https://api.github.com/users/{username}/following'

    followers = get_github_users(followers_url, token)
    following = get_github_users(following_url, token)

    return followers, following

your_github_username = 'RitabrataDas343'
your_personal_access_token = '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'

followers, following = get_github_followers_and_following(your_github_username, your_personal_access_token)

# if followers:
#     print(f"GitHub Followers: {len(followers)}")
#     i = 1
#     for follower in followers:
#         print(i, follower)
#         i = i + 1

# if following:
#     print(f"\nGitHub Following: {len(following)}")
#     i = 1
#     for followed in following:
#         print(i, followed)
#         i = i + 1

if followers and following:
    print("Persons who are following me, but I am not following them:\n")
    list1 = [item for item in followers if item not in following]
    i = 1
    for j in list1:
        print(i, j)
        i = i+1

    print("\nPersons whom I am following but they are not following me:\n")
    list2 = [item for item in following if item not in followers]
    i = 1
    for j in list2:
        print(i, j)
        i = i+1




