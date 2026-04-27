const API = "http://127.0.0.1:5000/api";

async function createBlock() {
    const data = document.getElementById("blockData").value;

    const res = await fetch(`${API}/block`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ data })
    });

    const result = await res.json();
    alert(JSON.stringify(result, null, 2));
}

async function loadChain() {
    const res = await fetch(`${API}/chain`);
    const data = await res.json();

    document.getElementById("chainOutput").innerText =
        JSON.stringify(data, null, 2);
}

async function validateChain() {
    const res = await fetch(`${API}/validate`);
    const data = await res.json();

    document.getElementById("validationResult").innerText =
        data.valid ? "Valid ✅" : "Invalid ❌";
}

async function hashData() {
    const data = document.getElementById("hashData").value;

    const res = await fetch(`${API}/hash`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ data })
    });

    const result = await res.json();

    document.getElementById("hashResult").innerText =
        "Hash: " + result.hash;
}