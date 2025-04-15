async function getTags() {
    const keyword = document.getElementById("keyword").value.trim();
    if (!keyword) {
        alert("Masukkan kata kunci dulu!");
        return;
    }

    const res = await fetch("/get_tags", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ keyword })
    });

    const data = await res.json();
    if (data.tags) {
        const tagString = data.tags.join(", ");
        document.getElementById("tagsOutput").textContent = tagString;
        document.getElementById("result").style.display = "block";
    } else {
        alert("Gagal mengambil tag.");
    }
}

function copyTags() {
    const text = document.getElementById("tagsOutput").textContent;
    navigator.clipboard.writeText(text).then(() => {
        alert("Tags berhasil disalin ke clipboard!");
    });
}
