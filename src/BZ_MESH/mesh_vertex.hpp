/**
 * @file mesh_vertex.hpp
 * @author Rémi Helleboid (remi.helleboid@st.com)
 * @brief
 * @version 0.1
 * @date 2022-07-14
 *
 * @copyright Copyright (c) 2022
 *
 */

#pragma once

#include <algorithm>
#include <iostream>
#include <map>
#include <string>
#include <vector>

#include "vector.hpp"

namespace bz_mesh {

class Vertex {
 private:
    /**
     * @brief Index of the vertex within the mesh.
     *
     */
    std::size_t m_index;

    /**
     * @brief Position of the k-vector.
     *
     */
    vector3 m_position;

    /**
     * @brief The energy of the band with index b_idx at this vertex
     * is stored as m_band_energies[b_idx].
     * For example, m_band_energies[3] is the energy of the band 3 at the k-point with position m_position.
     *
     */
    std::vector<double> m_band_energies;

 public:
    /**
     * @brief Default constructor of a new Vertex object.
     *
     */
    Vertex() : m_index{0}, m_position{} {}

    /**
     * @brief Construct a new Vertex object with a given index.
     *
     * @param index
     */
    explicit Vertex(std::size_t index) : m_index(index), m_position{} {}

    /**
     * @brief Construct a new Vertex object with a given index and position.
     *
     * @param index
     * @param postion
     */
    Vertex(std::size_t index, const vector3& position) : m_index(index), m_position{position} {}

    /**
     * @brief Construct a new Vertex object with a given index and position (x, y, z).
     *
     * @param index
     * @param x
     * @param y
     * @param z
     */
    Vertex(std::size_t index, double x, double y, double z) : m_index(index), m_position{x, y, z} {}

    /**
     * @brief Get the index of the vertex.
     *
     * @return std::size_t
     */
    std::size_t get_index() const { return m_index; }

    /**
     * @brief Get the position of the vertex.
     *
     * @return vector3
     */
    const vector3& get_position() const { return m_position; }

    /**
     * @brief Add an energy at the end of the list of energy. (One energy per band).
     *
     * @param energy
     */
    void add_band_energy_value(double energy) { m_band_energies.push_back(energy); }

    /**
     * @brief Set the band energy at a given band index.
     *
     * @param index_band
     * @param new_energy
     */
    void set_band_energy(std::size_t index_band, double new_energy) {
        if (index_band > m_band_energies.size()) {
            throw std::invalid_argument("The energy of valence band " + std::to_string(index_band) +
                                        " cannot be modify because it does not exists.");
        }
        m_band_energies[index_band] = new_energy;
    }

    /**
     * @brief Get the number of band energies stored in the Vertex object.
     *
     * @return std::size_t
     */
    std::size_t get_number_bands() const { return m_band_energies.size(); }

    /**
     * @brief Get the energy at band index.
     *
     * @param band_index
     * @return double
     */
    double get_energy_at_band(std::size_t band_index) const { return m_band_energies[band_index]; }
};

}  // namespace bz_mesh