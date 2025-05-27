import google.generativeai as genai
from prompt import formulate_prompt

class SemanticRetriever():
    def __init__(self, vector_store, topk):
        self.vector_store = vector_store
        self.topk = topk

    def search(self, query):
        docs = self.vector_store.similarity_search(query, k=self.topk)
        return [doc.page_content for doc in docs]

class QuestionAnswer:
    def __init__(self, vector_store):
        
        self.retriever = SemanticRetriever(vector_store, topk=4)
            
        # self.reranker = Ranker(topk=3)
        generation_config = {
            "temperature": 0.9,
            "top_p": 1,
            "top_k": 3,
        }

        self.gemini = genai.GenerativeModel(model_name="gemini-2.5-flash-preview-05-20",
                                       generation_config=generation_config,)

    def get_final_prompt(self, query):
        final_docs = self.retriever.search(query)
        # final_docs = self.reranker.get_final_docs(query, docs)

        return formulate_prompt(query, final_docs)
    
    def get_answer(self, query):
        final_prompt = self.get_final_prompt(query)

        gemini_response = self.gemini.generate_content(
            final_prompt
        )
        
        return gemini_response.candidates[0].content.parts[0].text