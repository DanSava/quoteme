var steem = require('steem');

const wif = process.env.SPK
const parentAuthor  = "" // Leave empty for new post
const author = "littlebitscience"
const permlink = "little-bitscience-facts-test-2"
const title = "Here we go again!"
const body = `

# ${title}

----

***How about them apples*** 

![](https://steemitimages.com/0x0/https://spee.ch/a/science-facts-1.jpeg)

### So you liked this small nugget of knowledge. What next?
I will try to post daily a small an interesting science fact. So you can follow me if you want to see more. 

You know another great science factoid that you would like to share with me leave it in the comments. I will greatly appreciate it 

Let me know how I can improve. 
>Nobody starts out knowledgeable, we all struggle to gain knowledge as we move forward! 

### Check out some older *little* science facts:
[older posts link here]

<table>
<tr><td>Pat on the head</td><td><b>Upvote this post</b></td><td> https://media1.tenor.com/images/153e9bdd80008e8c0f94110450fcbf98/tenor.gif?itemid=10534102 </td></tr>
<tr><td>Spread the knowledge:</td><td><b>Resteem is just one click away</b></td></tr>
<tr><td>Follow me at:</td><td><b>@littlebitscience</b></td></tr>
</table>

`
const parentPermlink = "science" // If it is new post this will be the same as the first post tag. 

const jsonMetadata = {
    tags: ['funny', 'informative', 'education', 'fun'],
    app: 'littelbitsciencefacts'
}

steem.broadcast.comment(wif, parentAuthor, parentPermlink, author, permlink, title, body, jsonMetadata, function(err, result) {
    console.log(err, result);
  });

// steem.api.getAccounts([username], function(err, result) {
//     console.log(err, result);
// });

