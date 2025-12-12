from rest_framework.views import APIView
from rest_framework.response import Response
import requests

class RagQueryView(APIView):
    def post(self, request):
        question = request.data.get("question")

        # send to your GPU server LLM/RAG endpoint
        # change URL to your actual GPU server
        response = requests.post(
            "http://YOUR_GPU_SERVER:8001/rag/query",
            json={"question": question},
        )

        return Response(response.json())
