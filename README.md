

This project formats simple arithmetic problems (addition and subtraction) in a clean vertical layout — just like how you'd see them in a primary school math notebook.

## 🧠 What It Does

The function `arithmetic_arranger()` takes a list of up to five arithmetic problems and formats them vertically and side-by-side. It can also optionally display the answers.

### ✅ Example Output

```python
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
diff
Copy
Edit
   32      3801      45      123
+ 698    -    2    + 43    +  49
-----    ------    ----    -----
With show_answers=True:

python
Copy
Edit
arithmetic_arranger(["32 + 8", "1 - 3801", "9999 + 9999", "523 - 49"], True)
yaml
Copy
Edit
  32         1      9999      523
+  8    - 3801    + 9999    -  49
----    ------    ------    -----
  40     -3800     19998      474
🚧 Error Handling
This function handles various user input errors:

❌ More than five problems → "Error: Too many problems."

❌ Unsupported operators → "Error: Operator must be '+' or '-'."

❌ Non-digit characters → "Error: Numbers must only contain digits."

❌ Operands longer than four digits → "Error: Numbers cannot be more than four digits."

🔧 Tech Used
Python 3

String formatting & validation logic

