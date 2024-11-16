import "./App.css";
import { useEffect, useState } from "react";

interface StockTransaction {
  transactions: {
    id: number;
    code: string;
    date: Date;
    last_transaction: string;
    max_transaction: string;
    min_transaction: string;
    avg_transaction: string;
    cash_flow_per: string;
    quantity: string;
    cash_flow: string;
  }[];
}

function App() {
  const [transactions, setTransactions] = useState<StockTransaction>({
    transactions: [],
  });

  useEffect(() => {
    const fetchTransactions = async () => {
      try {
        const response = await fetch("http://localhost:3000/api/transactions");
        if (!response.ok) {
          throw new Error("Failed to fetch data");
        }
        const data = await response.json();
        console.log(data);
        setTransactions(data);
      } catch (err) {
        console.log("An error occurred while fetching data: " + err);
      }
    };

    fetchTransactions();
  }, []);

  return (
    <>
      {transactions.transactions.map((t) => (
        <div key={t.id}>{t.code}</div>
      ))}
    </>
  );
}

export default App;
