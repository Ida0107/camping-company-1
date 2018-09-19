let list = []

$(function(){
  $(".bool").on('change', function() {
  if ($(this).is(':checked')) {
    $(this).attr('value', 'True');
  } else {
    $(this).attr('value', 'False');
  }
})
});

$(function(){
var inputs = document.getElementsByTagName("input");
for(var i = 0; i < inputs.length; i++) {
    if(inputs[i].type == "checkbox" ) {
        if (inputs[i].value === "True"){
			var att = document.createAttribute("checked");
att.value = "checked";
inputs[i].setAttributeNode(att);
        }
    }
}
});

$(function(){
  $(".info-bundle").children("button").click(function() {
    if ($(this).text() === "Add To Itinerary"){
        $(this).text("Added")
        list.push($(this).siblings("input[type='number']").val())
    } else {
       $(this).text("Add To Itinerary")
       list.pop($(this).siblings("input[type='number']").val())
       }
    localStorage.setItem("choices",list)
  })
})

$(document).ready(function() {
       $("#test").submit(function(e){
            e.preventDefault()
            var CSRFtoken = $('input[name=csrfmiddlewaretoken]').val();
            var x = ""
            $.ajax({
                 type:"POST",
                 url:"/user/itinerary/",
                 data: {
                        places: localStorage.getItem("choices"),
                         csrfmiddlewaretoken: CSRFtoken

                        },
                 success: function(data){
                     alert("choice taken")
                 }
            });
            localStorage.setItem("choices", "")
             $(this).hide()
             $("#tests").toggleClass("test")
            return false;
       });
 })