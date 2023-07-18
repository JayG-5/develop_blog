document.addEventListener("DOMContentLoaded", function () {
  const editor = new toastui.Editor({
    el: document.querySelector("#editor"),
    initialEditType: "markdown",
    height: "400px",
  });

  // '완료' 버튼 클릭 시, 에디터 내용을 서버로 전송하는 함수
  function submitContent() {
    // const title = document.querySelector('#id_title').value;

    const title = "test123";
    const body = editor.getMarkdown();
    fetch("/write/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
        "X-CSRFToken": "{{ csrf_token }}",
      },
      body: JSON.stringify({ title, body }),
    })
      .then((response) => response.json())
      .then((data) => {
        // 글 작성이 완료되면 필요한 동작 수행
      })
      .catch((error) => {
        console.error("Error:", error);
      });
  }

  // '완료' 버튼 클릭 이벤트를 등록
  const submitButton = document.querySelector("#submit-button");
  if (submitButton) {
    submitButton.addEventListener("click", submitContent);
  }
});
