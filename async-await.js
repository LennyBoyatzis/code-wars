const fetch = require('node-fetch');
const TEST_URL = 'https://jsonplaceholder.typicode.com/posts/1';
const fetch_posts = fetch(TEST_URL)
    .then((response) => {
      return response.json() 
    })

async function do_async() {
    const posts = await fetch_posts
    console.log("Done", posts)

    const places = "some string"
    console.log("places", places)
}

function crackOn() {
  console.log("cracking on")
}

do_async()
crackOn()
