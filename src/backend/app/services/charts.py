import pandas as pd
import matplotlib.pyplot as plt
import io
import base64
import seaborn as sns
from matplotlib.ticker import FuncFormatter


class ChartsService:
    @staticmethod
    def grafico_checkup_time():
        try:
            file_path = "./temp/MERGE_Final.csv"
            df = pd.read_csv(file_path)
            delta_columns = [
                col
                for col in df.columns
                if col.startswith(
                    ("delta_ZP5", "delta_ZP5A", "delta_ZP6", "delta_CABINES")
                )
            ]
            df["total_checkup_time"] = df[delta_columns].sum(axis=1)
            df_sample = df.sample(20)

            sns.set_style("whitegrid")
            plt.figure(figsize=(14, 7))
            barplot = sns.barplot(
                x="KNR", y="total_checkup_time", data=df_sample, palette="viridis"
            )
            plt.title(
                "Tempo Total de Check-up por Carro (Amostra de 20 Carros)",
                fontsize=16,
                fontweight="bold",
            )
            plt.xlabel("KNR (Identificação do Carro)", fontsize=12)
            plt.ylabel("Tempo Total de Check-up (minutos)", fontsize=12)
            plt.xticks(rotation=45, fontsize=9)
            plt.yticks(fontsize=9)
            plt.tight_layout()

            formatter = FuncFormatter(lambda y, _: f"{y:,.0f}")
            barplot.yaxis.set_major_formatter(formatter)

            buffer = io.BytesIO()
            plt.savefig(buffer, format="png", dpi=300)
            plt.close()
            buffer.seek(0)
            image_png = buffer.getvalue()
            buffer.close()

            graphic = base64.b64encode(image_png)
            graphic = graphic.decode("utf-8")

            return graphic

        except FileNotFoundError:
            return f"Error: File '{file_path}' not found."
        except pd.errors.EmptyDataError:
            return f"Error: The file '{file_path}' is empty."
        except Exception as e:
            return f"An error occurred: {e}"

    @staticmethod
    def grafico_freq_erros():
        try:
            file_path = "./temp/FALHAS_KNR.csv"
            df_falhas = pd.read_csv(file_path)
            group_counts = df_falhas["S_GROUP_ID"].value_counts()
            threshold = 0.05
            total_counts = group_counts.sum()
            small_groups = group_counts[group_counts < threshold * total_counts]
            group_counts_adjusted = group_counts.drop(small_groups.index)
            group_counts_adjusted["Outros"] = small_groups.sum()

            plt.figure(figsize=(8, 8))
            colors = sns.color_palette("pastel")[0 : len(group_counts_adjusted)]
            plt.pie(
                group_counts_adjusted,
                labels=group_counts_adjusted.index,
                autopct="%1.1f%%",
                startangle=140,
                colors=colors,
                wedgeprops={"edgecolor": "white"},
                textprops={"fontsize": 10},
            )
            centre_circle = plt.Circle((0, 0), 0.70, fc="white")
            fig = plt.gcf()
            fig.gca().add_artist(centre_circle)
            plt.title(
                "Grupos de Falhas Mais Recorrentes", fontsize=16, fontweight="bold"
            )
            plt.tight_layout()

            buffer = io.BytesIO()
            plt.savefig(buffer, format="png", dpi=300)
            plt.close()
            buffer.seek(0)
            image_png = buffer.getvalue()
            buffer.close()

            graphic = base64.b64encode(image_png)
            graphic = graphic.decode("utf-8")

            return graphic

        except FileNotFoundError:
            return f"Error: File '{file_path}' not found."
        except pd.errors.EmptyDataError:
            return f"Error: The file '{file_path}' is empty."
        except Exception as e:
            return f"An error occurred: {e}"
