var steem = require('steem');

const wif = process.env.SPK
const parentAuthor  = "" // Leave empty for new post
const author = "littlebitscience"
const permlink = "little-bitscience-facts-test-2"
const title = "Here we go again!"
const body = `
# This will blow your minddd

***image goes here*** 

<table>
<tr><td>Some Text</td><td><b>Text text text </b></td></tr>
<tr><td>Some Text</td><td><b>Text text text </b></td></tr>
<tr><td>Some Text</td><td><b>Text text text </a></b></td></tr>
<tr><td>Some Text</td><td><b>Text text text</b></td></tr>
<tr><td>Follow</td><td><b>@littlebitscience</b></td></tr>
</table>`
const parentPermlink = "interesting" // If it is new post this will be the same as the first post tag. 

const jsonMetadata = {
    tags: ['testing', 'fun'],
    app: 'littelbitsbot'
}

steem.broadcast.comment(wif, parentAuthor, parentPermlink, author, permlink, title, body, jsonMetadata, function(err, result) {
    console.log(err, result);
  });

// steem.api.getAccounts([username], function(err, result) {
//     console.log(err, result);
// });