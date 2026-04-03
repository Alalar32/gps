setTimeout(() => {
  const alerts = document.querySelectorAll(".messages.pop");
  alerts.forEach((alert) => {
    alert.classList.add("hidden");
  });
}, 3000);
function openModal() {
  document.getElementById("modal").classList.remove("hidden");
}

function closeModal() {
  document.getElementById("modal").classList.add("hidden");
}

function saveStudent() {
  const name =
    document.getElementById("first_name").value +
    " " +
    document.getElementById("last_name").value;

  const id = document.getElementById("student_id").value;
  const age = document.getElementById("age").value;
  const studentClass = document.getElementById("Class").value;
  const gender = document.getElementById("Gender").value;
  const Pname = document.getElementById("Pname").value;
  const Pcontact = document.getElementById("Pcontact").value;
  const Pemail = document.getElementById("Pemail").value;
  const emailWarning = document.getElementById("emailwarning");

  if (
    !name ||
    !id ||
    !age ||
    !studentClass ||
    !gender ||
    !Pname ||
    !Pcontact ||
    !Pemail
  )
    return alert("Please fill in all fields!");

  if (Pemail && !/\S+@\S+\.\S+/.test(Pemail)) {
    emailWarning.classList.remove("hidden");
    return;
  } else {
    emailWarning.classList.add("hidden");
  }
}

function switchView(view) {
  document.querySelectorAll(".view-section").forEach((section) => {
    section.classList.remove("active");
  });
  document.getElementById(`${view}-view`).classList.add("active");
  const pageTitle = {
    students: "Manage Students",
    reports: "Academic Reports",
    attendance: "Attendance",
    schedule: "Class Schedule",
  };
  document.getElementById("page-title").textContent = pageTitle[view];
}

function searchstudents() {
  const query = document.getElementById("searchInput").value;
  if (query) {
    document.getElementById("Form").submit();
    const input = document.getElementById("searchInput");
    if (input) {
      input.focus();
    }
  }
}


  document.addEventListener('DOMContentLoaded', function() {
    const navButtons = document.querySelectorAll('.nav-btn');
    navButtons.forEach(button => {
      button.addEventListener('click', function() {
        navButtons.forEach(btn => btn.classList.remove('active'));
        this.classList.add('active');
      });
    });
  });
