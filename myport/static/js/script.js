document.addEventListener('DOMContentLoaded', function(){

const loginBtn = document.getElementById('login-modal');
const loginModal = document.querySelector("[data-modal]");
const closeModal = document.querySelector('.close-modal');

<<<<<<< HEAD
//  open modal 
loginBtn.addEventListener('click', ()=>{
     loginModal.showModal()
})
=======

if (loginBtn != null) {
    //  open modal 
loginBtn.addEventListener('click', ()=>{
    loginModal.showModal()
})
}
>>>>>>> 2619a3918320ef852ef3d49de35081a6e110ccb9
 
//  close modal 
closeModal.addEventListener('click', () =>{
    loginModal.close()
})

// close modal on all side 
loginModal.addEventListener("click", function(e) {
    const dialogDimensions = loginModal.getBoundingClientRect()
   if (
     e.clientX < dialogDimensions.left ||
     e.clientX > dialogDimensions.right ||
      e.clientY < dialogDimensions.top ||
      e.clientY > dialogDimensions.bottom
    ) {
        loginModal.close()
    }

 })


<<<<<<< HEAD
=======





 

>>>>>>> 2619a3918320ef852ef3d49de35081a6e110ccb9
// End of Domcontentloaded
})


// function to open post modal form
const postModal = document.querySelector("[data-post-modal]");
function openPostModal(){
    postModal.showModal();
}

const closePostModal = document.querySelector('.close-post-modal');

//  close modal 
closePostModal.addEventListener('click', () =>{
    postModal.close()
 })


 // close modal on all side 
 postModal.addEventListener("click", function(e) {
    const dialogDimensions = postModal.getBoundingClientRect()
   if (
     e.clientX < dialogDimensions.left ||
     e.clientX > dialogDimensions.right ||
      e.clientY < dialogDimensions.top ||
      e.clientY > dialogDimensions.bottom
    ) {
        postModal.close()
    }
 })




<<<<<<< HEAD

=======
>>>>>>> 2619a3918320ef852ef3d49de35081a6e110ccb9
function portSideNav(){

    const portSideBar = document.querySelector('.port-side-nav');
     if ( portSideBar.style.display == 'none'){
         portSideBar.style.display = 'block'; 
      } else {
         portSideBar.style.display = 'none';
      
         }


         
    
}

function closeNav(){
    const portSideBar = document.querySelector('.port-side-nav');
     if ( portSideBar.style.display == 'block'){
         portSideBar.style.display = 'none'; 
      } else {
         portSideBar.style.display = 'block';
      
         }
}
<<<<<<< HEAD
=======















>>>>>>> 2619a3918320ef852ef3d49de35081a6e110ccb9
//  admin page
function getCookie(name) {
    var cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        var cookies = document.cookie.split(';');
        for (var i = 0; i < cookies.length; i++) {
            var cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
var csrftoken = getCookie('csrftoken');



var activeItem = null;

<<<<<<< HEAD
function buildList(){
    var wrapper = document.querySelector('.list-wrapper');
    wrapper.innerHTML = '';
    var url = 'http://172.105.190.111:8000/api/post/post-list/'
    
=======

function buildList(){
    var wrapper = document.querySelector('.list-wrapper');
    wrapper.innerHTML = ''

   
    var url = 'http://localhost:8000/api/post/post-list/'
>>>>>>> 2619a3918320ef852ef3d49de35081a6e110ccb9
    fetch(url)
    .then(response => response.json())
    .then((data) => {
        

        var list = data
       

        for ( i in list ){
            var item = `
            <div class="d-flex" id="data-row-${i}" >
            <div class="p-2 flex-fill flex-grow-1 title">${list[i].title} </div>
            
            <div> 
            <button class="p-2 flex-fill btn-info mb-1 edit"><i class="fa-regular fa-pen-to-square"></i></button>
            <button class="p-2 flex-fill btn-danger mb-1 delete"><i class="fa-solid fa-trash"></i></button>
            </div>
          </div><hr>
            `

<<<<<<< HEAD
            wrapper.innerHTML += item;

=======
                wrapper.innerHTML += item;
             
>>>>>>> 2619a3918320ef852ef3d49de35081a6e110ccb9
        }
        //  at the end of the first loop do another loop to solve the problem of single click

        for ( i in list ){ 
              // Attach event listeners after all elements are added
        var editBtn = document.getElementsByClassName('edit')[i];
        var deleteBtn = document.getElementsByClassName('delete')[i];
       
        //  UPDATE BUTTONS HERE
        editBtn.addEventListener('click', (function(item){
            return function (){
                updatePost(item);
            }
        })(list[i]))

        // Delete button here 

        deleteBtn.addEventListener('click', (function(item){
            return function (){
                deleteItem(item);
            }
        })(list[i]))


        }

    })
    .catch((error) => console.log(error))
    

}

buildList();


//====================================================================
//  CREATING POST FORM
// ==================================================================

// start buiding the form inside the modal 

var postForm = document.getElementById('postForm');
postForm.addEventListener('submit', function(e){
    e.preventDefault();
    console.log('Form submission triggered');

<<<<<<< HEAD
    var url = 'http://172.105.190.111:8000/api/post/post-create/';
    if (activeItem != null){
        var url = `http://172.105.190.111:8000/api/post/post-update/${activeItem.id}/`
=======
    var url = 'http://localhost:8000/api/post/post-create/';
    if (activeItem != null){
        var url = `http://localhost:8000/api/post/post-update/${activeItem.id}/`
>>>>>>> 2619a3918320ef852ef3d49de35081a6e110ccb9
        activeItem = null
    }



    var formData = new FormData(postForm);

<<<<<<< HEAD



    fetch(url, {
        method: 'POST',
        headers: {
            'X-CSRFToken': csrftoken,
        },
=======
    fetch(url, {
        method: 'POST',
>>>>>>> 2619a3918320ef852ef3d49de35081a6e110ccb9
        body: formData
    })
    .then(function(response) {
        if (!response.ok) {
            throw new Error('Network response was not ok.');
        }
        return response.json(); // Assuming the server returns JSON
    })
    .then(function(data) {
        // Handle success response
        console.log('Success:', data);
        // Optionally, you can perform actions after successful form submission
        const postModal = document.querySelector("[data-post-modal]");
        postModal.close();
        buildList();
        document.getElementById('postForm').reset();
    })
    .catch(function(error) {
        // Handle error
        console.error('Error:', error);
    });
    
});


// Function to generate slug from title
function generateSlug(title) {
    return title.toLowerCase().replace(/\s+/g, '-').replace(/[^\w-]+/g, '');
}

// Get elements
const titleInput = document.getElementById('title');
const slugInput = document.getElementById('slug');

// Event listener to auto-generate slug based on title
titleInput.addEventListener('input', function () {
    const titleValue = titleInput.value.trim();
    const generatedSlug = generateSlug(titleValue);
    slugInput.value = generatedSlug;
});

 

// Create the update 
// ===============================================
// POST ADMIN UPDATE
// ================================================

function updatePost(item){
    activeItem = item;
    console.log(activeItem)
    const postModal = document.querySelector("[data-post-modal]");
        postModal.showModal();

        // Assuming activeItem properties correspond to form field IDs
    document.getElementById('title').value = activeItem.title || '';
    document.getElementById('slug').value = activeItem.slug || '';
    document.getElementById('description').value = activeItem.description || '';
    document.getElementById('embed_code').value = activeItem.embed_code || '';
    // Set other form fields accordingly
        
}




function deleteItem(item){
<<<<<<< HEAD
    var url = `http://172.105.190.111:8000/api/post/post-delete/${item.id}/`
=======
    var url = `http://localhost:8000/api/post/post-delete/${item.id}/`
>>>>>>> 2619a3918320ef852ef3d49de35081a6e110ccb9
    var options = {
        method: 'DELETE',
        headers: {
            'Content-type': 'application/json', 
            'X-CSRFToken': csrftoken,
        }
    }

   fetch(url, options)
   .then((response)=>{
    buildList()
   })
}
<<<<<<< HEAD
=======


 

function initMap() {
    const location = { lat: -19.27829600021189, lng: 146.81108351278175 };
    const map = new google.maps.Map(document.getElementById("map"), {
        center: location,
        zoom: 15,
    });
    const marker = new google.maps.Marker({
        position: location,
        map: map,
        title: "Townsville, Qld, Australia",
    });
}

// Call the function to initialize the map
initMap();
>>>>>>> 2619a3918320ef852ef3d49de35081a6e110ccb9
