function required()
{
var FName = document.forms["donateform"]["FName"].value;
var LName = document.forms["donateform"]["LName"].value;
var age = document.forms["donateform"]["age"].value;
var Gender = document.forms["donateform"]["gender"].value;
var Mobile = document.forms["donateform"]["Mobile"].value;
var Email = document.forms["donateform"]["Email"].value;
var group = document.forms["donateform"]["group"].value;
var mailformat = /^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$/;
var re = /^\(?(\d{3})\)?[- ]?(\d{3})[- ]?(\d{4})$/;

if (FName == ""&& Fname==null)
{
alert("Enter The First Name");
}

else if (LName == ""&& LName ==null)
{
alert("Enter The Last Name");
}

else if (age == ""&& age ==null)
{
alert("Enter The Age");
}

else if (Gender == ""&& Gender ==null)
{
alert("Choose Gender ");
}

else if (Mobile == "" && Mobile ==null && !inputText.value.match(re) )
{
alert("Enter the Mobile Number ");
}

else if (Email== ""&& Email==null && !inputText.value.match(mailformat))
{
alert("Enter Valid Email ");
}

else if (group == ""&&group ==null)
{
alert("Set The Password");
}

else 	
{
alert('Donated Sucessfull...!');

}
}