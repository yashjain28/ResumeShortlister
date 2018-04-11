# Resume Shortlister

A handy tool for shortlisting best resumes based on keywords. Easily find a whether an applicant match the required skills for your current opening.

## How to use it? 

(Currently compatible only for mac-users, future versions might support windows).

Clone this repository into your local-PC and extract it. Go to config.json file and edit it based on your requirement. For example:

```javascript
{
   "threshold": 6,
   "keyword_to_score": {
        "react":2,
        "REST":2,
        "angularjs":5,
        "nodejs":3
    }
}
``` 
Set your required threshold based on the keywords and their weight you set. 
Make sure all the .pdf files you want to look into are in this folder as well. 

Then just run `./shortList.sh`

### Pre-Requisites 

Must have python2 installed


## How this works?

Current version, tokenizes words and checks if the word is in the list of required keywords. Each keyword is assigned a weight, which helps calculating the final score. 

Once score is calculated for each file, shortlisting can be based on a threshold. 

 
  