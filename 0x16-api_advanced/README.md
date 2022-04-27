# API Advanced
In this project I will be making advanced API calls to Reddit API using python3 scripts.
At the end of this project I will be able to:
- Read API documentation to find the endpoints you’re looking for
- Use an API with pagination
- To parse JSON results from an API
- Make a recursive API call
- Sort a dictionary by value
## Files:
* **0. How many subs?**
[0-subs.py](./0-subs.py): Script that queries the [Reddit API](https://www.reddit.com/dev/api/) and returns the number of subscribers for a given subreddit.

* **1. Top Ten**
[1-top_ten.py](./1-top_ten.py): Script that queries the [Reddit API](https://www.reddit.com/dev/api/) and prints the titles of the first 10 hot posts listed for a given subreddit.

* **2. Recurse it!**
[2-recurse.py](./2-recurse.py): Script that recursively queries the [Reddit API](https://www.reddit.com/dev/api/) and returns a list containing the titles of all hot articles for a given subreddit.

* **3. Count it!**
[100-count.py](./100-count.py): Script that recursively queries the [Reddit API](https://www.reddit.com/dev/api/) parses the tile of all hot articles, and prints a sorted count of given keywords..

**Test files for:**
* [0-subs.py](./tests/0-main.py)
* [1-top_ten.py](./tests/1-main.py)
* [2-recurse.py](./tests/2-main.py)
* [100-count.py](./tests/100-main.py)

## Example usage
$ python3 0-main.py programming
756024
