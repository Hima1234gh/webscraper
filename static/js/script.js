let tagData = {};

async function fetchTags() {
    const url = document.getElementById("url").value;

    const res = await fetch("/get-tags", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ url })
    });

    tagData = await res.json();

    const tagSelect = document.getElementById("tag");
    tagSelect.innerHTML = "";

    Object.keys(tagData).forEach(tag => {
        const opt = document.createElement("option");
        opt.value = tag;
        opt.textContent = tag;
        tagSelect.appendChild(opt);
    });

    updateClasses();
}

function updateClasses() {
    const tag = document.getElementById("tag").value;
    const classSelect = document.getElementById("class");

    classSelect.innerHTML = "";

    const empty = document.createElement("option");
    empty.value = "";
    empty.textContent = "No class";
    classSelect.appendChild(empty);

    tagData[tag].forEach(cls => {
        const opt = document.createElement("option");
        opt.value = cls;
        opt.textContent = cls;
        classSelect.appendChild(opt);
    });
}

async function scrape() {
    const data = {
        url: document.getElementById("url").value,
        tag: document.getElementById("tag").value,
        class: document.getElementById("class").value
    };

    const res = await fetch("/scrape", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(data)
    });

    const result = await res.json();
    const output = document.getElementById("output");
    output.innerHTML = "";

    result.forEach(item => {
        const li = document.createElement("li");
        li.textContent = item;
        output.appendChild(li);
    });
}
