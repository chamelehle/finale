var ExampleApplication = React.createClass({
   render: function() {
     var listItems = this.props.data.comments.map(function(item){
       return (
         <li key={item.comment}</li>
       )
     });
     return <ul style={{"marginLeft":"0.5in"}}>{listItems}</ul>
   }
 });


 var ExampleApplicationFactory = React.createFactory(ExampleApplication);

 var start = new Date().getTime();
 var update = setInterval(function() {
  $.ajax({
    url: "/comments",
    success: function(data) {
      ReactDOM.render(
          ExampleApplicationFactory({data: data}),
          document.getElementById('commented'));
    }
  })
}, 500);
