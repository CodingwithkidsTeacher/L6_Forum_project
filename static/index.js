function send(endpoint) {
  // Gather the values the user typed into the post form.
  // NOTE: this assumes post.html has inputs with these ids:
  //   id="name"    -> the poster's name
  //   id="subject" -> the post subject
  //   id="post"    -> the post body text
  // Adjust these ids to match your actual post.html if they differ.
  var name = document.getElementById('name').value;
  var subject = document.getElementById('subject').value;
  var post = document.getElementById('post').value;
 
  var data = {
    name: name,
    subject: subject,
    post: post
  };
 
  var xhr = new XMLHttpRequest();
  xhr.open('POST', endpoint, true);
  xhr.setRequestHeader('Content-Type', 'application/json');
 
  xhr.onreadystatechange = function () {
    if (xhr.readyState === 4 && xhr.status === 200) {
      // The server re-renders the whole page (with the new post included)
      // and sends back the full HTML. Swap it in so the page updates
      // instantly without a manual refresh.
      document.open();
      document.write(xhr.responseText);
      document.close();
    }
  };
 
  xhr.send(JSON.stringify(data));
}
