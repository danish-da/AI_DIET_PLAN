from django.shortcuts import render
from  ai_diet_plan import settings
from pandas import read_excel, read_csv

from openai import OpenAI
import openai

# Create your views here.

api_key = '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'

def chat_with_gpt(prompt):
    client = OpenAI(

        # This is the default and can be omitted
        api_key=api_key,

    )
    chat_completion = client.chat.completions.create(

        messages=[

            {
                "role": "user",
                "content": prompt,

            }
        ],
        model="gpt-3.5-turbo",
    )

    print(chat_completion.choices[0].message.content)
    res = chat_completion.choices[0].message.content

    return res


def predict(request):
    if request.method=='POST':
        a1=request.POST.get('q1')
        print(a1)
        a2=request.POST.get('q2')
        print (a2)
        a3= request.POST.get('q3')
        print(a3)
        a4 = request.POST.get('q4')
        print(a4)
        a5 = request.POST.get('q5')
        print(a5)
        a6 = request.POST.get('q6')
        print(a6)
        a7 = request.POST.get('q7')
        print(a7)
        imgpath = str(settings.BASE_DIR) + str(settings.STATIC_URL) + "Dataset.csv"
        data = read_csv(imgpath, "Dataset")
        print(data.columns)
        X = data.iloc[:, 0:7].values
        y = data.iloc[:, 7].values

        test = [float(a1), float(a2), float(a3), float(a4), float(a5), float(a6), float(a7)]
        from sklearn.tree import DecisionTreeRegressor
        regressor = DecisionTreeRegressor(random_state=0)
        regressor.fit(X, y)
        res = regressor.predict([test])

        print(res[0])
        ans = chat_with_gpt(res)
        context = {
            'kk': res[0],
            'des': ans
        }
        return render(request, 'predict/results.html', context)
    return render(request, 'predict/prediction.html')




