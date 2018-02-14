# Reddit Collector
This program is design to collect all data from a subreddit and organize the
data by submissions, user comments. Below I will provide extecution commands
as well as the output file format.

## Commands

**Subreddit:** `-s | --subreddit` will allow the user to select which subreddit
they want to extract data from
* Default: /r/all

**Limit:** `-l | --limit` will allow the user to select the amount of submissions
they want to retrieve.
* Default: None, which will retrieve all submissions

## Execution

```
python run.py --subreddit=catan -l=5
```

## Output

For a quick live data example please run the execution command above to retrieve a small
example file.

**Psuedo Output Format:**
```
{
  "subreddit_name": [
    {
      "submission_id": [
        {
          "submission_title": "...",
          "submission_text": "...",
          "submission_timestamp": "YYYY-MM-DD HH:mm:SS",
          "comments": [
            {
              "User_Name_1": [
                {
                    "comment_1_id": [
                      "comment_timestamp": "...",
                      "comment_text": ".." 
                    ],
                    "comment_2_id": [
                      "comment_timestamp": "...",
                      "comment_text": ".." 
                    ]
                }
              ],
              "User_Name_2": [
                {
                    "comment_1_id": [
                      "comment_timestamp": "...",
                      "comment_text": ".." 
                    ],
                    "comment_2_id": [
                      "comment_timestamp": "...",
                      "comment_text": ".." 
                    ]
                }
              ]
            }
           ]
         }
      ]
    }
  ]
}
```