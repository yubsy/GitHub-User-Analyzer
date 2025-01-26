import requests

def get_github_user_info():
    # Asks for user name
    username = input("Enter your GitHub user name: ")

    try:
        # Get list of followers
        followers_url = f"https://api.github.com/users/{username}/followers"
        followers_response = requests.get(followers_url)
        followers_response.raise_for_status()
        followers = [follower['login'] for follower in followers_response.json()]

        # Get a list of public repositories
        repos_url = f"https://api.github.com/users/{username}/repos?type=owner&sort=updated"
        repos_response = requests.get(repos_url)
        repos_response.raise_for_status()
        repos = [repo['name'] for repo in repos_response.json()]

        # Obtain general user information
        user_url = f"https://api.github.com/users/{username}"
        user_response = requests.get(user_url)
        user_response.raise_for_status()
        user_data = user_response.json()
        email = user_data.get('email', 'No public email available')
        bio = user_data.get('bio', 'No bio available')
        company = user_data.get('company', 'No company specified')
        location = user_data.get('location', 'No location specified')
        public_repos = user_data.get('public_repos', 0)
        followers_count = user_data.get('followers', 0)
        following_count = user_data.get('following', 0)

        # View results
        print(f"\nInformation from {username}:")
        print(f"- Email: {email}")
        print(f"- Bio: {bio}")
        print(f"- Company: {company}")
        print(f"- Location: {location}")
        print(f"- Public Repositories: {public_repos}")
        print(f"- Followers: {followers_count}")
        print(f"- Following: {following_count}")

        print(f"\nFollowers of {username}:")
        for follower in sorted(followers):
            print(f"- {follower}")

        print(f"\nPublic repositories of {username}:")
        for repo in repos:
            print(f"- {repo}")

    except requests.exceptions.RequestException as e:
        print(f"Error accessing the API: {e}")

# Call the function
if __name__ == "__main__":
    get_github_user_info()
